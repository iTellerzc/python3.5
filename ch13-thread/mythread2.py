#! /usr/bin/python3
#-*-coding:UTF-8-*-

import _thread
from time import sleep
from datetime import datetime

loops=[4,2]
date_time_format = '%y-%m-%d %H:%M:%S'

def date_time_str(date_time):
	return datetime.strftime(date_time, date_time_format)

def loop(n_loop, n_sec, lock):
	print('线程(', n_loop,') 开始执行：', date_time_str(datetime.now()), ', 先休眠（', n_sec, ')秒')
	sleep(n_sec)
	print('线程(', n_loop,') 休眠结束, 结束于：', date_time_str(datetime.now()))
	lock.release()

def main():
	print('-----------所有线程开始时间：', date_time_str(datetime.now()))
	locks = []
	n_loops = range(len(loops))

	for i in n_loops:
		lock=  _thread.allocate_lock()
		lock.acquire()
		locks.append(lock)

	for i in n_loops:
		_thread.start_new_thread(loop, (i, loops[i], locks[i]))

	for i in n_loops:
		while locks[i].locked():
			print('locked not release!')
			pass

	print('-----------所有线程结束时间：', date_time_str(datetime.now()))

if __name__ == '__main__':
	main()