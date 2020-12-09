#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - check list if it has a cycle
 *
 * @list: linked list
 *
 * Return: 0 if no and 1 if yes
 */

int check_cycle(listint_t *list)
{
	listint_t *shortterm, *longterm;

	if (list == NULL)
		return (0);

	if (list == list->next)
		return (1);

	shortterm = list;
	longterm = list;

	while (longterm->next != NULL)
	{
		shortterm = shortterm->next;
		longterm = longterm->next;
		if (longterm->next == NULL)
			break;
		longterm = longterm->next;
		if (shortterm == longterm)
			return (1);
	}
	return (0);
}
