# loggy
Live Streaming of Logs to multiple hosts
log_check.py has the main logic for checking and parsing fresh logs from the log file. It parse's file once and keeps on parsing from where the pointer left if any changes are detected.

view.py throws the data as a Json Response.
