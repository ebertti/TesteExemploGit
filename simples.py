import psutil, time


def main():
    for i in range(100):
        time.sleep(1)
        print(psutil.disk_io_counters())

if __name__ == '__main__':
    main()
