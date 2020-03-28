package implementations_java;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.Arrays;

import org.junit.jupiter.api.Test;

class HeapTest {

	@Test
	void min_heap_test() {
		System.out.println("Testing Min Heap");
		Heap h= new MinHeap();
		System.out.println("Testing insert, peek, and poll");
		h.insert(5);
		h.insert(0);
		h.insert(10);
		h.insert(20);
		h.insert(-100);
		h.insert(0);
		h.insert(200);
		int[] arr= h.toArray();
		System.out.println("Array after inserting: " + Arrays.toString(arr));
		assertTrue(Heap.checkMinHeap(arr));
		int peek= h.peek();
		assertEquals(peek, -100);
		int item= h.poll();
		assertEquals(item, -100);
		arr= h.toArray();
		System.out.println("Array after deleting one element: " + Arrays.toString(arr));
		assertTrue(Heap.checkMinHeap(arr));
		item= h.poll();
		assertEquals(item, 0);
		arr= h.toArray();
		System.out.println("Array after deleting two elements: " + Arrays.toString(arr));
		assertTrue(Heap.checkMinHeap(arr));
		item= h.poll();
		assertEquals(item, 0);
		peek= h.peek();
		assertEquals(peek, 5);

		System.out.println("Insert, peek, and poll tests complete");
	}

	@Test
	void max_heap_test() {
		Heap h= new MaxHeap();
		System.out.println("Testing Max Heap");
		System.out.println("Testing insert, peek, and poll");
		h.insert(5);
		h.insert(0);
		h.insert(10);
		h.insert(20);
		h.insert(-100);
		h.insert(0);
		h.insert(200);
		int[] arr= h.toArray();
		System.out.println("Array after inserting: " + Arrays.toString(arr));
		assertTrue(Heap.checkMaxHeap(arr));
		int peek= h.peek();
		assertEquals(peek, 200);
		int item= h.poll();
		assertEquals(item, 200);
		arr= h.toArray();
		System.out.println("Array after deleting one element: " + Arrays.toString(arr));
		assertTrue(Heap.checkMaxHeap(arr));
		item= h.poll();
		assertEquals(item, 20);
		arr= h.toArray();
		System.out.println("Array after deleting two elements: " + Arrays.toString(arr));
		assertTrue(Heap.checkMaxHeap(arr));
		item= h.poll();
		assertEquals(item, 10);
		peek= h.peek();
		assertEquals(peek, 5);

		System.out.println("Insert, peek, and poll tests complete");
	}

}
