
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class ExecutorFrameworkDemo {

    static class Worker implements Runnable {
        private final int taskId;

        Worker(int taskId) {
            this.taskId = taskId;
        }

        @Override
        public void run() {
            System.out.println(
                "Task " + taskId + " started by "
                + Thread.currentThread().getName()
            );

            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                System.out.println("Task " + taskId + " was interrupted.");
                return;
            }

            System.out.println(
                "Task " + taskId + " completed by "
                + Thread.currentThread().getName()
            );
        }
    }

    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(3);

        System.out.println("Submitting tasks to the thread pool...");

        for (int i = 1; i <= 6; i++) {
            executor.execute(new Worker(i));
        }

        executor.shutdown();

        try {
            if (executor.awaitTermination(10, TimeUnit.SECONDS)) {
                System.out.println("All tasks completed.");
            } else {
                System.out.println("Some tasks did not finish in time.");
                executor.shutdownNow();
            }
        } catch (InterruptedException e) {
            executor.shutdownNow();
            Thread.currentThread().interrupt();
        }
    }
}
