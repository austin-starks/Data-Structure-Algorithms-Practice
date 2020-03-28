/**
 *
 */
package implementations_java;

import java.util.Arrays;

abstract class Heap {
	/** The current maximum size of the heap */
	private int maxSize= 10;

	/** The current size of the heap */
	protected int size= 0;

	/** An array representing the internal structure of the heap */
	protected int[] items= new int[10];

	/** Swaps two elements in the items array (the internal representation of the heap)
	 *
	 * @param index1: the index of the first item to swap
	 * @param index2: the index of the second item to swap */
	protected void swap(int index1, int index2) {
		int tmp= items[index1];
		items[index1]= items[index2];
		items[index2]= tmp;
	}

	/** Gets the index of the left child from parent index
	 *
	 * @param parentIndex: the index to get the left child index from.
	 * @return the index of the left child */
	protected static int getLeftChildIndex(int parentIndex) {
		return 2 * parentIndex + 1;
	}

	/** Gets the index of the right child from parent index
	 *
	 * @param parentIndex: the index to get the right child index from.
	 * @return the index of the right child */
	protected static int getRightChildIndex(int parentIndex) {
		return 2 * parentIndex + 2;
	}

	/** Gets the index of the parent from the child index
	 *
	 * @param childIndex: the index to get the parent index from
	 * @return the index of the parent element */
	protected static int getParentIndex(int childIndex) {
		return (childIndex - 1) / 2;
	}

	/** Says whether the child index has a parent
	 *
	 * @param parentIndex: the index of the parent
	 * @return True if the index of child index has a parent (i.e, if it's the root index). False
	 *         otherwise */
	protected boolean hasParent(int childIndex) {
		return getParentIndex(childIndex) >= 0;
	}

	/** Says whether the parent index has a left child
	 *
	 * @param parentIndex: the index of the parent
	 * @return True if the index of parent index has a left child. False otherwise */
	protected boolean hasLeftChild(int parentIndex) {
		return getLeftChildIndex(parentIndex) < size;
	}

	/** Says whether the parent index has a right child
	 *
	 * @param parentIndex: the index of the parent
	 * @return True if the index of parent index has a right child. False otherwise */
	protected boolean hasRightChild(int parentIndex) {
		return getRightChildIndex(parentIndex) < size;
	}

	/** Gets the value of the parent from the child's index.
	 *
	 * @param childtIndex: the index position of the child element
	 * @return the element that is the parent of the child index */
	protected int parent(int childIndex) {
		return items[getParentIndex(childIndex)];
	}

	/** Gets the value of the left child from the parent index
	 *
	 * @param parentIndex: the index position of the parent element
	 * @return the element that is the left child of parent index */
	protected int leftChild(int parentIndex) {
		return items[getLeftChildIndex(parentIndex)];
	}

	/** Gets the value of the right child from the parent index
	 *
	 * @param parentIndex: the index position of the parent element
	 * @return the element that is the right child of parent index */
	protected int rightChild(int parentIndex) {
		return items[getRightChildIndex(parentIndex)];
	}

	/** Ensures the internal array has enough elements; if it doesn't, it creates a new array with
	 * double the maximum size. */
	private void ensureSpace() {
		if (size >= maxSize) {
			items= Arrays.copyOf(items, maxSize * 2);
			maxSize= maxSize * 2;
		}
	}

	/** Returns the top item of the heap.
	 *
	 * If this is a min-heap, this function returns the smallest item of the heap. If this is a
	 * max-heap, this function returns the largest item of the heap.
	 *
	 * @return the top item of the heap */
	public int peek() {
		if (size > 0) {
			return items[0];
		} else {
			throw new IllegalStateException();
		}
	}

	/** Removes the top item of the heap.
	 *
	 * If this is a min-heap, this function removes and returns the smallest item of the heap. If this
	 * is a max-heap, this function removes and returns the largest item of the heap.
	 *
	 * @return the top item of the heap */
	public int poll() {
		if (size == 0) {
			throw new IllegalStateException();
		} else {
			int item= items[0];
			size-- ;
			items[0]= items[size];
			bubbleDown();
			return item;
		}
	}

	/** Inserts a number into the heap.
	 *
	 * @param num the number to add to the heap */
	public void insert(int num) {
		ensureSpace();
		items[size]= num;
		size++ ;
		bubbleUp();
	}

	/** Returns an array representation of this heap
	 *
	 * @return a copy of the array representation of this heap. */
	public int[] toArray() {
		return Arrays.copyOf(items, size);
	}

	/** Checks to see if the array arr represents a min heap
	 *
	 * This function recursively checks to see if the input array is a valid min heap.
	 *
	 * @param arr the array to check
	 * @return true if the array is a min-heap. False otherwise */
	public static boolean checkMinHeap(int[] arr) {
		boolean result= checkMinHeap(arr, 0);
		return result;
	}

	private static boolean checkMinHeap(int[] arr, int index) {
		// if this index doesn't have a right child... it's a leaf node.
		if (getRightChildIndex(index) >= arr.length) { return true; }

		// otherwise, recursively check if the left and right children
		// are heaps
		boolean left= arr[index] <= arr[getLeftChildIndex(index)] && checkMinHeap(arr, getLeftChildIndex(index));
		boolean right= arr[index] <= arr[getRightChildIndex(index)] && checkMinHeap(arr, getRightChildIndex(index));
		return left && right;
	}

	/** Checks to see if the array arr represents a max heap
	 *
	 * This function recursively checks to see if the input array is a valid max heap.
	 *
	 * @param arr the array to check
	 * @return true if the array is a min-heap. False otherwise */
	public static boolean checkMaxHeap(int[] arr) {
		boolean result= checkMaxHeap(arr, 0);
		return result;
	}

	private static boolean checkMaxHeap(int[] arr, int index) {
		// if this index doesn't have a right child... it's a leaf node.
		if (getRightChildIndex(index) >= arr.length) { return true; }

		// otherwise, recursively check if the left and right children
		// are heaps
		boolean left= arr[index] >= arr[getLeftChildIndex(index)] && checkMaxHeap(arr, getLeftChildIndex(index));
		boolean right= arr[index] >= arr[getRightChildIndex(index)] && checkMaxHeap(arr, getRightChildIndex(index));
		return left && right;
	}

	abstract void bubbleUp();

	abstract void bubbleDown();
}
