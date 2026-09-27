public class ThreadSum {

    static class SumWorker extends Thread {

        private long start;
        private long end;
        private long result;

        public SumWorker(long start, long end) {
            this.start = start;
            this.end = end;
        }

        @Override
        public void run() {

            System.out.println(
                getName() + " calculating from " + start + " to " + end
            );

            long sum = 0;

            for (long i = start; i <= end; i++) {
                sum += i;
            }

            result = sum;

            System.out.println(
                getName() + " finished."
            );
        }

        public long getResult() {
            return result;
        }
    }

    public static void main(String[] args) throws InterruptedException {

        long startTime = System.nanoTime();

        SumWorker thread1 = new SumWorker(1, 1_000_000);
        SumWorker thread2 = new SumWorker(1_000_001, 2_000_000);
        SumWorker thread3 = new SumWorker(2_000_001, 3_000_000);
        SumWorker thread4 = new SumWorker(3_000_001, 4_000_000);

        thread1.setName("Thread 1");
        thread2.setName("Thread 2");
        thread3.setName("Thread 3");
        thread4.setName("Thread 4");

        thread1.start();
        thread2.start();
        thread3.start();
        thread4.start();

        thread1.join();
        thread2.join();
        thread3.join();
        thread4.join();

        long total =
                thread1.getResult()
                + thread2.getResult()
                + thread3.getResult()
                + thread4.getResult();

        long endTime = System.nanoTime();

        double executionTime =
                (endTime - startTime) / 1_000_000_000.0;

        System.out.println("\n=== RESULTS ===");
        System.out.println("Total Sum: " + total);
        System.out.println(
            "Execution Time: " + executionTime + " seconds"
        );
    }
}