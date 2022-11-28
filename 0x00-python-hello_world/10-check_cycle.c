#include "lists.h"

/**
 * check_cycle - frees a listint_t list
 * @list: pointer to list to be freed
 * Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
listint_t * temp;
if(!list)
{
return (0);
}
temp = list;
while(temp->next != list && temp->next != NULL)
{
temp->next = temp->next->next;
}
if(temp->next == NULL)
{
return (0);
}
return(1);
}
