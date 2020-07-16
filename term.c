#include <vte/vte.h>

// jesus. that was sick.
// it's deficiency, not improvement.
// can I define func inside func?
int true = 1;
// must not zero.
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
    VteTerminal *sampler = VTE_TERMINAL(terminal);
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
    const char *data_s = "sample\n";
    gssize gsd = 7;
    vte_terminal_feed(sampler, data_s, gsd);
    // or just not to start anything?
    // does have the fucking writing! mother fuck!
    // there's shit! nothing returns.
    printf("hello world!\n");
    // check each individual shits.
    // you can pass the handle to another process. spawn??
    /* Connect some signals */
    g_signal_connect(window, "delete-event", gtk_main_quit, NULL);
    const char *data_0s = "sampleZ\n";
    gssize gsz = 8;
    vte_terminal_feed(sampler, data_0s, gsz);
    g_signal_connect(terminal, "child-exited", gtk_main_quit, NULL);
    const char *data_s0 = "sampleX\n";
    // gssize gsz = 8;
    // called what?
    // has offset on the overall shit.
    // does not appear anything related to buffer till main.
    vte_terminal_feed(sampler, data_s0, gsz);
    /* Put widgets together and run the main loop */
    gtk_container_add(GTK_CONTAINER(window), terminal);
    const char *data_s1 = "sampleY\n";
    // gssize gsz = 8;
    vte_terminal_feed(sampler, data_s1, gsz);
    gtk_widget_show_all(window);
    const char *data_s2 = "sampleK\n";
    // gssize gsz = 8;
    // do this before the main session?
    // I don't even start the fuck!
    // how can you get things done then?
    vte_terminal_feed(sampler, data_s2, gsz);
    // gdk_threads_add_idle();
    int samp()
    {
        // while (true)
        for (int counter = 0; counter < 30; ++counter)
        {
            printf("hello world!\n");
            sleep(1); //cool. -> not responding before it is done.
            // this is in seconds.
            // not even again.
            // no fucking gui anymore???
            // but accepting the change somehow?
        }
        return 0;
        // it should be doing this repeatedly.
        // maybe we should repeat this process over and over again?
    };
    g_timeout_add(1000, samp, NULL);
    // fucking shit. it is not working as a separate thread.
    // not fucking responding! -> try 3 times.
    // not to rush???
    gtk_main();
    // not reached here.
    // maybe the same for that thing.
    // spawn a process and then feed back into the terminal!
    printf("hello world!\n");
}
