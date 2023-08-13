#include "lists.h"

/**
 * reverse_listint - this function reverses linked list
 * @head: it points to the first node in the list
 * Return: pointer to 1st node
 */
void reverse_listint(listint_t **head)
{
	listint_t *old = NULL;
	listint_t *curr = *head;
	listint_t *next = NULL;

	while (curr)
	{
		next = curr->next;
		curr->next = old;
		old = curr;
		curr = next;
	}

	*head = old;
}

/**
 * is_palindrome - this function checks if linked list is palindrome
 * @head: double pointer to linked list
 * Return: 1 palindrome, 0 not palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *duplicate = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			duplicate = slow->next;
			break;
		}
		if (!fast->next)
		{
			duplicate = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverse_listint(&duplicate);

	while (duplicate && temp)
	{
		if (temp->n == duplicate->n)
		{
			duplicate = duplicate->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!duplicate)
		return (1);

	return (0);
}
