package org.yinwang.pysonar;

import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;
import org.yinwang.pysonar.ast.PyModule;
import org.yinwang.pysonar.ast.Node;

import java.io.*;
import java.util.HashMap;
import java.util.Map;
import java.util.logging.Level;
import java.util.logging.Logger;


/**
 * Provides a factory for python source ASTs.  Maintains configurable on-disk and
 * in-memory caches to avoid re-parsing files during analysis.
 */
public class AstCache {

    private static final Logger LOG = Logger.getLogger(AstCache.class.getCanonicalName());

    @NotNull
    private Map<String, Node> cache = new HashMap<>();
    @NotNull
    private Parser parser = new Parser();

    public AstCache() {
    }


    /**
     * Clears the memory cache.
     */
    public void clear() {
        cache.clear();
    }


    /**
     * Removes all serialized ASTs from the on-disk cache.
     *
     * @return {@code true} if all cached AST files were removed
     */
    public boolean clearDiskCache() {
        try {
            $.deleteDirectory(new File(Analyzer.self.cacheDir));
            return true;
        } catch (Exception x) {
            LOG.log(Level.SEVERE, "Failed to clear disk cache: " + x);
            return false;
        }
    }


    public void close() {
        parser.close();
        clearDiskCache();
    }


    /**
     * Returns the syntax tree for {@code path}.  May find and/or create a
     * cached copy in the mem cache or the disk cache.
     *
     * @param path absolute path to a source file
     * @return the AST, or {@code null} if the parse failed for any reason
     */
    @Nullable
    public Node getAST(@NotNull String path) {
        // Cache stores null value if the parse failed.
        if (cache.containsKey(path)) {
            return cache.get(path);
        }

        // Might be cached on disk but not in memory.
        Node node = getSerializedModule(path);
        if (node != null) {
            LOG.log(Level.FINE, "reusing " + path);
            cache.put(path, node);
            return node;
        }

        node = null;
        try {
            LOG.log(Level.FINE, "parsing " + path);
            node = parser.parseFile(path);
        } finally {
            cache.put(path, node);  // may be null
        }

        if (node != null) {
            serialize(node);
        }

        return node;
    }


    /**
     * Each source file's AST is saved in an object file named for the MD5
     * checksum of the source file.  All that is needed is the MD5, but the
     * file's base name is included for ease of debugging.
     */
    @NotNull
    public String getCachePath(@NotNull String sourcePath) {
        return $.makePathString(Analyzer.self.cacheDir, $.getFileHash(sourcePath));
    }


    // package-private for testing
    void serialize(@NotNull Node ast) {
        String path = getCachePath(ast.file);
        ObjectOutputStream oos = null;
        FileOutputStream fos = null;
        try {
            fos = new FileOutputStream(path);
            oos = new ObjectOutputStream(fos);
            oos.writeObject(ast);
        } catch (Exception e) {
            $.msg("Failed to serialize: " + path);
        } finally {
            try {
                if (oos != null) {
                    oos.close();
                } else if (fos != null) {
                    fos.close();
                }
            } catch (Exception e) {
            }
        }
    }


    // package-private for testing
    @Nullable
    PyModule getSerializedModule(String sourcePath) {
        if (!new File(sourcePath).canRead()) {
            return null;
        }
        File cached = new File(getCachePath(sourcePath));
        if (!cached.canRead()) {
            return null;
        }
        return deserialize(sourcePath);
    }


    // package-private for testing
    @Nullable
    PyModule deserialize(@NotNull String sourcePath) {
        String cachePath = getCachePath(sourcePath);
        FileInputStream fis = null;
        ObjectInputStream ois = null;
        try {
            fis = new FileInputStream(cachePath);
            ois = new ObjectInputStream(fis);
            return (PyModule) ois.readObject();
        } catch (Exception e) {
            return null;
        } finally {
            try {
                if (ois != null) {
                    ois.close();
                } else if (fis != null) {
                    fis.close();
                }
            } catch (Exception e) {

            }
        }
    }
}
