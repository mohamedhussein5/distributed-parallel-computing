
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class Client {
    public static void main(String[] args) {
        String host = "localhost";
        int port = 5000;

        try (
            Socket socket = new Socket(host, port);
            BufferedReader input = new BufferedReader(
                new InputStreamReader(socket.getInputStream()));
            PrintWriter output = new PrintWriter(
                socket.getOutputStream(), true)
        ) {
            System.out.println("Connected to the server.");

            output.println("Hello from the client!");
            System.out.println("Message sent to server.");

            String response = input.readLine();
            System.out.println("Server response: " + response);

        } catch (Exception e) {
            System.out.println("Client error: " + e.getMessage());
        }
    }
}
