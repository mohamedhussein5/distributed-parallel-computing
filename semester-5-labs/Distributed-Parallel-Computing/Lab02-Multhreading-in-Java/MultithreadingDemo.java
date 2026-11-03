public class MultithreadingDemo {

    static class Worker extends Thread {

        private final int workerNumber;

        public Worker(int workerNumber) {
            this.workerNumber = workerNumber;
        }

        @Override
        public void run() {
            System.out.println("Thread " + workerNumber + " started.");

            for (int i = 1; i <= 5; i++) {
                System.out.println("Thread " + workerNumber +
                        " is processing task " + i);

                try {
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    System.out.println("Thread " + workerNumber + " was interrupted.");
                }
            }

            System.out.println("Thread " + workerNumber + " finished.");
        }
    }

    public static void main(String[] args) throws InterruptedException {

        Worker thread1 = new Worker(1);
        Worker thread2 = new Worker(2);
        Worker thread3 = new Worker(3);
        Worker thread4 = new Worker(4);

        thread1.start();
        thread2.start();
        thread3.start();
        thread4.start();

        thread1.join();
        thread2.join();
        thread3.join();
        thread4.join();

        System.out.println("\nAll threads have completed.");
    }
}