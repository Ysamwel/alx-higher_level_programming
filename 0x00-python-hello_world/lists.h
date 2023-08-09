#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - its is asingly linked list
 * @n: an integer
 * @next: a pointer to the next node
 */
/*tempelate*/
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

/*prototypes*/
size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif
