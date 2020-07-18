import java.io.*;

public class Terminal {

    class ReaderConsole implements Runnable {
        private InputStream is;

        public ReaderConsole(InputStream is) {
            this.is = is;
        }

        public void run() {
            InputStreamReader isr = null;
            try {
                isr = new InputStreamReader(is, "utf8");
                // hey! how about a byte reader?
            } catch (UnsupportedEncodingException e1) {
                e1.printStackTrace();
            }
            BufferedReader br = new BufferedReader(isr);

            int c = -1;
            try {
                while ((c = br.read()) != -1) {
                    System.out.println("WELCOME_Y");
                    System.out.print((char) c);
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    class WrittenConsole implements Runnable {
        private OutputStream os;

        public WrittenConsole(OutputStream os) {
            this.os = os;
        }

        public void run() {
            try {
                while (true) {
                    String line = this.getConsoleLine();
                    line += "\n";
                    System.out.println("WELCOME_X");
                    byte[] bts = line.getBytes();
                    os.write(bts);
                    System.out.println(bts);
                    os.flush();
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        private String getConsoleLine() throws IOException {
            String line = null;
            InputStreamReader input = new InputStreamReader(System.in);
            BufferedReader br = new BufferedReader(input);
            line = br.readLine();
            return line;
        }
    }

    // can you find the stderr?
    public void execute() throws Exception {
        String[] cmds = { "bash" };
        Process process = Runtime.getRuntime().exec(cmds);
        InputStream is = process.getInputStream();
        OutputStream os = process.getOutputStream();
        InputStream es = process.getErrorStream();

        Thread t1 = new Thread(new ReaderConsole(is));
        Thread t0 = new Thread(new ReaderConsole(es));
        Thread t2 = new Thread(new WrittenConsole(os));
        t1.start();
        t0.start();
        t2.start();
        // great then. whatever.
    }

    public static void main(String[] args) {
        System.out.println("WELCOME");
        // not as effective as I expected.
        Terminal t = new Terminal();
        try {
            System.out.println("AGAIN");
            t.execute();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}