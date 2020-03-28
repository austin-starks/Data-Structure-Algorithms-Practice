package implementations_java;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class HashMapTest {

	@Test
	void test() {
		HashMap<String, String> h= new HashMap<>();
		System.out.println("Testing HashMaps");
		System.out.println("Testing add, get, and size");

		System.out.println(" - Test adding 1 element");
		h.add("math", "A");
		assertEquals(h.size(), 1);
		assertEquals(h.get("math"), "A");

		System.out.println(" - Test getting element that doesn't exist");
		assertEquals(h.get("science"), null);

		System.out.println(" - Test adding a different element");
		h.add("science", "B+");
		assertEquals(h.get("science"), "B+");
		assertEquals(h.size(), 2);

		System.out.println(" - Test overriding an element");
		h.add("science", "B");
		assertEquals(h.size(), 2);
		assertEquals(h.get("science"), "B");

		System.out.println(" - Test removing an element");
		assertEquals(h.remove("science"), "B");
		assertEquals(h.size(), 1);
		assertEquals(h.get("science"), null);

		System.out.println(" - Test removing an element that doesn't exist");
		assertEquals(h.remove("social studies"), null);
		assertEquals(h.size(), 1);
		System.out.println("Testing add, get, and size complete");

		System.out.println("Test load factor and rehashing");
		h.add("english", "A-");
		h.add("art", "C+");
		h.add("computer science", "B");
		h.add("history", "A+");
		h.add("geography", "N/A");
		assertEquals(h.getLoadFactor(), 0.6);
		h.add("geology", "B-");
		assertEquals(h.getLoadFactor(), 0.35);
		assertEquals(h.size(), 7);
		assertEquals(h.get("history"), "A+");
		assertEquals(h.get("art"), "C+");
		assertEquals(h.get("zoology"), null);
		System.out.println("Test load factor and rehashing complete");
		System.out.println("Test HashMap complete");

	}

}
