class ConfigCheck(object):

    disable_functions = [
        "apache_setenv",
        "chdir",
        "chgrp",
        "chmod",
        "chown",
        "copy",
        "curl_exec",
        "curl_init",
        "dl",
        "error_log",
        "exec",
        "fclose",
        "file_put_contents",
        "fopen",
        "ftp_connect",
        "ftp_exec",
        "fwrite",
        "glob",
        "ignore_user_abort",
        "imap_mail",
        "imap_open",
        "ini_get",
        "ini_get_all",
        "ini_set",
        "link",
        "linkinfo",
        "mail",
        "mb_send_mail",
        "passthru",
        "pcntl_alarm",
        "pcntl_async_signals",
        "pcntl_exec",
        "pcntl_fork",
        "pcntl_get_last_error",
        "pcntl_getpriority",
        "pcntl_setpriority",
        "pcntl_signal",
        "pcntl_signal_dispatch",
        "pcntl_signal_get_handler",
        "pcntl_sigprocmask",
        "pcntl_sigtimedwait",
        "pcntl_sigwaitinfo",
        "pcntl_strerror",
        "pcntl_wait",
        "pcntl_waitpid",
        "pcntl_wexitstatus",
        "pcntl_wifcontinued",
        "pcntl_wifexited",
        "pcntl_wifsignaled",
        "pcntl_wifstopped",
        "pcntl_wstopsig",
        "pcntl_wtermsig",
        "pfsockopen",
        "phpinfo",
        "popen",
        "proc_get_status",
        "proc_open",
        "putenv",
        "readlink",
        "rename",
        "set_time_limit",
        "shell_exec",
        "sqlite_open",
        "sqlite_popen",
        "stream_socket_server",
        "symlink",
        "syslog",
        "system",
        "xml_parse",
        "xml_parser_create",
        "xml_parser_create_ns"
    ]

    def __init__(self):
        super(ConfigCheck, self).__init__()

    def check_functions(self, funcs):
        funcs = funcs.split(",")
        for func in self.disable_functions:
            if func not in funcs:
                print("%s may skip" % func)