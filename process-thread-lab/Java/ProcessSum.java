import java.io.BufferedReader;
import java.io.InputStreamReader;

public class ProcessSum {

    public static void main(String[] args) throws Exception {

        // Worker mode: calculate a specific range
        if (args.length == 2) {

            long start = Long.parseLong(args[0]);
            long end = Long.parseLong(args[1]);

            long sum = 0;

            for (long i = start; i <= end; i++) {
                sum += i;
            }

            System.out.println(sum);
            return;
        }

        // Main process
        long startTime = System.nanoTime();

        long[][] ranges = {
            {1, 1_000_000},
            {1_000_001, 2_000_000},
            {2_000_001, 3_000_000},
            {3_000_001, 4_000_000}
        };

        Process[] processes = new Process[4];

        for (int i = 0; i < 4; i++) {

            ProcessBuilder builder = new ProcessBuilder(
                "java",
                "-cp",
                ".",
                "ProcessSum",
                String.valueOf(ranges[i][0]),
                String.valueOf(ranges[i][1])
            );

            processes[i] = builder.start();

            System.out.println(
                "Process " + (i + 1)
                + " started for range "
                + ranges[i][0]
                + " to "
                + ranges[i][1]
            );
        }

        long total = 0;

        for (int i = 0; i < 4; i++) {

            BufferedReader reader = new BufferedReader(
                new InputStreamReader(
                    processes[i].getInputStream()
                )
            );

            String result = reader.readLine();

            processes[i].waitFor();

            long partialSum = Long.parseLong(result);

            total += partialSum;

            System.out.println(
                "Process " + (i + 1)
                + " finished. Result: "
                + partialSum
            );
        }

        long endTime = System.nanoTime();

        double executionTime =
            (endTime - startTime) / 1_000_000_000.0;

        System.out.println("\n=== RESULTS ===");
        System.out.println("Total Sum: " + total);
        System.out.println(
            "Execution Time: "
            + executionTime
            + " seconds"
        );
    }
}