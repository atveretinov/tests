# void quickSortR(T* a, long N) {
# // На входе - массив a[], a[N] - его последний элемент.
#
#   long i = 0, j = N-1; 		// поставить указатели на исходные места
#   T temp, p;
#
#   p = a[ N>>1 ];		// центральный элемент
#
#   // процедура разделения
#   do {
#     while ( a[i] < p ) i++;
#     while ( a[j] > p ) j--;
#
#     if (i <= j) {
#       temp = a[i]; a[i] = a[j]; a[j] = temp;
#       i++; j--;
#     }
#   } while ( i<=j );
#
#
#   // рекурсивные вызовы, если есть, что сортировать
#   if ( j > 0 ) quickSortR(a, j);
#   if ( N > i ) quickSortR(a+i, N-i);
# }

# TODO: add start and end indexes
def quickSort(array, N):

    i = 0
    j = N - 1
    p = int(array[N/2])

    while i <= j:
        while array[i] < p:
            i = i+1

        while array[j] > p:
            j = j-1

        if i <= j:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            i = i + 1
            j = j - 1

    if j > 0:
        quickSort(array,j)

    if i < N:







if __name__ == "__main__":
    array = [5, 1, 2, 3, 10, 4, 8, 9, 7, 6]

    quickSort(array, len(array))
    print(array)