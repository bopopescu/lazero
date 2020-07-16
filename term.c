#include <vte/vte.h>

// jesus. that was sick.
// it's deficiency, not improvement.
int main(int argc, char *argv[])
{
    GtkWidget *window, *terminal;
    // I hate all shits.
    // maybe this time we need a -> expression.
    //  gcc -O2 -Wall $(pkg-config --cflags vte-2.91) term.c -o term $(pkg-config --libs vte-2.91)
    // wrong shit. -> thank god!!!
    // gcc sample_terminal.c  -o sample_terminal -I/usr/include/vte-2.91 -I/usr/include/glib-2.0 -I/usr/lib/x86_64-linux-gnu/glib-2.0/include/ -I/usr/include/pango-1.0/ -I/usr/include/harfbuzz/ -I/usr/include/gtk-3.0/ -I/usr/include/cairo/ -I/usr/include/gdk-pixbuf-2.0 -I/usr/include/atk-1.0/
    /* Initialise GTK, the window and the terminal */
    gtk_init(&argc, &argv);
    terminal = vte_terminal_new(); // this one. check it.
    // how about check vte's source code?
    window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(window), "myterm");
    // you can print some shit, right?
    /* Start a new shell */
    // how to get the buffer somehow?
    // how to make the thing headless? -> server.
    // make it unstuck, when running a process. -> key to browse anything.
    VteTerminal *sampler =VTE_TERMINAL(terminal);
    // glong start_row = 0;
    // good again?
    // glong start_col = 0;
    // glong end_row = 100;
    // glong end_col = 100;
    // just fucking unused.
    gchar **envp = g_get_environ();
    gchar **command = (gchar *[]){g_strdup(g_environ_getenv(envp, "SHELL")), NULL};
    g_strfreev(envp);
    vte_terminal_spawn_async(sampler,
                             VTE_PTY_DEFAULT,
                             NULL,       /* working directory  */
                             command,    /* command */
                             NULL,       /* environment */
                             0,          /* spawn flags */
                             NULL, NULL, /* child setup */
                             NULL,       /* child pid */
                             -1,         /* timeout */
                             NULL, NULL, NULL);
// do another special shit?
const char *data_s="sample\n";
gssize gsz=7;
vte_terminal_feed(sampler,data_s,gsz);
// does have the fucking writing! mother fuck!
// there's shit! nothing returns.
printf("hello world!\n");
    // check each individual shits.
    // you can pass the handle to another process. spawn??
    /* Connect some signals */
    g_signal_connect(window, "delete-event", gtk_main_quit, NULL);
    g_signal_connect(terminal, "child-exited", gtk_main_quit, NULL);

    /* Put widgets together and run the main loop */
    gtk_container_add(GTK_CONTAINER(window), terminal);
    gtk_widget_show_all(window);
    gtk_main();
    // not reached here.
    printf("hello world!\n");
}
