#include <Windows.h>
#include <iostream>
#include <time.h>

const int N = 100;
int threads[N];
int first = 0, length = 0;

int need_run = 10;

DWORD WINAPI thread(void *arg);

void scheduler() {
	// Выбрать поток из очереди
	while (length > 0) {
		int thread_id = threads[first];

		first = (first+1 % N);
		length--;

		// Запускаем поток
		HANDLE h = CreateThread(NULL, 0, thread, &thread_id, 0, 0);

		// Ждем завершения
		WaitForSingleObject(h, INFINITE);
		CloseHandle(h);
	}
}

void Add2Queue(int id) {
	threads[ (first+length) % N ] = id;
	length++;
}

DWORD WINAPI thread(void *arg) {
	srand(GetTickCount());
	int thread_id = *(int*)arg;
	std::cout << "Поток " << thread_id << " работает" << std::endl;

	Sleep(1000);
	
	// Ставим на выполнение еще 2 потока
	if (need_run > 0) {
		int id1 = rand() % 30;
		std::cout << "Поток " << thread_id << " ставит в очередь поток " << id1 << std::endl;
		Add2Queue(id1);
		need_run--;
	}

	if (need_run > 0) {
		int id2 = rand() % 30;
		std::cout << "Поток " << thread_id << " ставит в очередь поток " << id2 << std::endl;
		Add2Queue(id2);
		need_run--;
	}

	Sleep(1000);

	return 0;
}

int main() {
	srand(GetTickCount());
	setlocale(0, "Russian");
	threads[0] = 0;
	first = 0; length = 1;
	scheduler();

	return 0;
}
