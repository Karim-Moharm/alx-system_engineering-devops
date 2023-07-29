#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>

/**
 * infinite_while - an infinite loop with delay 1sec
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * create_zombies - a function used to create 5 zombies processes
 */
void create_zombies(void)
{
	pid_t child_pid = 0;
	int count = 0;

	while (count < 5)
	{
		child_pid = fork();
		if (child_pid > 0)
			printf("Zombie process created, PID: %d\n", child_pid);
		else
			exit(0);
		count++;
	}
	infinite_while();
}

/**
 * main - entry function
 * Return: always 0
 */
int main(void)
{
	create_zombies();
	return (0);
}
