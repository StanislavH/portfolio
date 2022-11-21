#include <Windows.h>
#include <iostream>

const int N = 10;
HANDLE sem_full, sem_empty, mutex;

int counter = 0;
int buf[N];
int size;

const int gsteps = 10;

DWORD WINAPI producer(void *arg) {
	int steps = 0;
	while (steps < gsteps) {
		WaitForSingleObject(sem_empty, INFINITE);

		WaitForSingleObject(mutex, INFINITE);
		// Пишем
		int elem = rand() % 100;
		std::cout << "Пишем " << elem << std::endl;
		buf[counter] = elem;
		counter++;
		
		steps++;
		ReleaseMutex(mutex);

		ReleaseSemaphore(sem_full, 1, 0);
	}

	return 0;
}

DWORD WINAPI consumer(void *arg) {
	int steps = 0;
	while (steps < gsteps) {
		WaitForSingleObject(sem_full, INFINITE);

		WaitForSingleObject(mutex, INFINITE);
		// Читаем
		int elem = buf[counter-1];
		std::cout << "Читаем " << elem << std::endl;
		counter--;
		steps++;
		ReleaseMutex(mutex);

		ReleaseSemaphore(sem_empty, 1, 0);
	}

	return 0;
}

int main() {
	setlocale(0, "Russian");
	sem_empty = CreateSemaphore(0, N, N, 0);
	sem_full  = CreateSemaphore(0, 0, N, 0);
	mutex = CreateMutex(0, false, 0);

	HANDLE h1 = CreateThread(0, 0, producer, 0, 0, 0);
	HANDLE h2 = CreateThread(0, 0, consumer, 0, 0, 0);

	WaitForSingleObject(h1, INFINITE);
	WaitForSingleObject(h2, INFINITE);

	CloseHandle(h1);
	CloseHandle(h2);
	CloseHandle(sem_empty);
	CloseHandle(sem_full);
	CloseHandle(mutex);

	return 0;
}
