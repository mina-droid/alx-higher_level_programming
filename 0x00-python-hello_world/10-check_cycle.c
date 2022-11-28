#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - frees a listint_t list
 * @list: pointer to list to be freed
 * Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
listint_t ** temp;
temp = list;
while(list->next != NULL)
{
list->next = list.next;
}
if(list->next == temp)
{
return (1);
}
return(0);
}
