
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
    public static void main(String[] args) {
        int port = 5000;

        try (ServerSocket serverSocket = new ServerSocket(port)) {
            System.out.println("Server started on port " + port);
            System.out.println("Waiting for a client...");

            try (
                Socket socket = serverSocket.accept();
                BufferedReader input = new BufferedReader(
                    new InputStreamReader(socket.getInputStream()));
                PrintWriter output = new PrintWriter(
                    socket.getOutputStream(), true)
            ) {
                System.out.println("Client connected.");

                String message = input.readLine();
                System.out.println("Client says: " + message);

                output.println("Hello from the server! Message received.");
                System.out.println("Response sent to client.");
            }

        } catch (Exception e) {
            System.out.println("Server error: " + e.getMessage());
        }
    }
}
