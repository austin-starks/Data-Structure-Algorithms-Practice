package implementations_java;

public class MaxHeap extends Heap {

	/** Restores the heap property of this heap
	 *
	 * This function is invoked after an element is inserted into the heap. It travels up the heap until
	 * the inserted element is less than its parent. */
	@Override
	void bubbleUp() {
		int index= size - 1;
		while (hasParent(index) && parent(index) < items[index]) {
			swap(getParentIndex(index), index);
			index= getParentIndex(index);
		}
	}

	/** Restores the heap property of this heap
	 *
	 * This function is invoked after an element is deleted from the heap. Starting from the root, this
	 * function swaps positions with it's highest-valued child until the element is less than its
	 * children */
	@Override
	void bubbleDown() {
		int index= 0;
		while (hasLeftChild(index)) {
			int smallChildIndex= getLeftChildIndex(index);
			if (hasRightChild(index) && rightChild(index) > leftChild(index)) {
				smallChildIndex= getRightChildIndex(index);
			}
			if (items[index] > items[smallChildIndex]) {
				return;
			} else {
				swap(index, smallChildIndex);
			}
			index= smallChildIndex;
		}
	}

}
