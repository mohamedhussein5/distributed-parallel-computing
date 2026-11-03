
public class SynchronizationDemo {

    static class SharedCounter {
        private int count = 0;

        public synchronized void increment() {
            count++;
        }

        public int getCount() {
            return count;
        }
    }

    static class Worker extends Thread {
        private final SharedCounter counter;

        public Worker(SharedCounter counter, String name) {
            super(name);
            this.counter = counter;
        }

        @Override
        public void run() {
            for (int i = 0; i < 100000; i++) {
                counter.increment();
            }

            System.out.println(getName() + " finished.");
        }
    }

    public static void main(String[] args)
            throws InterruptedException {

        SharedCounter counter = new SharedCounter();

        Worker thread1 = new Worker(counter, "Thread 1");
        Worker thread2 = new Worker(counter, "Thread 2");
        Worker thread3 = new Worker(counter, "Thread 3");
        Worker thread4 = new Worker(counter, "Thread 4");

        thread1.start();
        thread2.start();
        thread3.start();
        thread4.start();

        thread1.join();
        thread2.join();
        thread3.join();
        thread4.join();

        System.out.println("Expected count: 400000");
        System.out.println("Actual count: " + counter.getCount());

        if (counter.getCount() == 400000) {
            System.out.println("Synchronization successful!");
        } else {
            System.out.println("Synchronization failed!");
        }
    }
}
