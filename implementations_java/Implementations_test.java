package implementations_java;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import java.util.Arrays;

import org.junit.jupiter.api.Test;

class Implementations_test {

	@Test
	void min_heap_test() {
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

}
