package implementations_java;

/** Implementation of HashMap using Linked Lists
 *
 * @author austin
 *
 * @param <K> The key of the item you're mapping
 * @param <V> The value corresponding to the key */
@SuppressWarnings("unchecked")
public class HashMap<K, V> {
	private Object[] bucketArray;
	private int numBuckets;
	private int size;
	private double loadFactor;
	private double maxLoad;

	public HashMap() {
		this.bucketArray= new Object[10];
		this.numBuckets= 10;
		this.size= 0;
		this.loadFactor= 0.0;
		this.maxLoad= 0.7;
	}

	public void setMaxLoad(double maxLoad) {
		assert maxLoad < 0.9 && maxLoad > 0.2;
		this.maxLoad= maxLoad;
	}

	public int getNumBuckets() {
		return numBuckets;
	}

	public double getLoadFactor() {
		return loadFactor;
	}

	public int size() {
		return size;
	}

	public boolean isEmpty() {
		return size == 0;
	}

	private int getArrayIndex(K key) {
		int index= key.hashCode();
		index= Math.floorMod(index, numBuckets);
		return index;
	}

	public Object[] getNodes(K key) {
		int index= getArrayIndex(key);
		HashNode<K, V> prev= null;
		HashNode<K, V> node= (HashNode<K, V>) bucketArray[index];
		while (node != null && !node.key.equals(key)) {
			prev= node;
			node= node.next;
		}
		return new Object[] { prev, node };
	}

	public V get(K key) {
		Object[] prev_node= getNodes(key);
		HashNode<K, V> node= (HashNode<K, V>) prev_node[1];
		return node == null ? null : node.value;
	}

	private void rehash() {
		loadFactor= 1.0 * size / numBuckets;
		if (loadFactor < maxLoad) { return; }
		numBuckets= 2 * numBuckets;
		Object[] oldArray= bucketArray;
		this.bucketArray= new Object[numBuckets];
		this.size= 0;
		for (int i= 0; i < numBuckets / 2; i++ ) {
			HashNode<K, V> node= (HashNode<K, V>) oldArray[i];
			while (node != null) {
				add(node.key, node.value);
				node= node.next;
			}
		}
	}

	public void add(K key, V value) {
		// gets node with the key of key and the node before that in the linked list
		Object[] prev_node= getNodes(key);
		HashNode<K, V> prev= (HashNode<K, V>) prev_node[0];
		HashNode<K, V> node= (HashNode<K, V>) prev_node[1];

		// if the node exists, change the value
		if (node != null) {
			node.value= value;
			return;
		}
		// if the node is null (doesn't already exist), add it to the linked list
		size++ ;
		HashNode<K, V> newNode= new HashNode<>(key, value);
		if (prev == null) {
			int index= getArrayIndex(key);
			bucketArray[index]= newNode;
		} else {
			prev.next= newNode;
		}
		rehash();
	}

	public V remove(K key) {
		// gets node with the key of key and the node before that in the linked list
		Object[] prev_node= getNodes(key);
		HashNode<K, V> node= (HashNode<K, V>) prev_node[1];
		HashNode<K, V> prev= (HashNode<K, V>) prev_node[0];

		// if the node is null, return null
		if (node == null) { return null; }

		// otherwise delete the node
		size-- ;
		HashNode<K, V> next= node.next;
		prev.next= next;
		return node.value;
	}

}

class HashNode<K, V> {
	K key;
	V value;

	// Reference to the next node
	HashNode<K, V> next;

	// Constructor
	public HashNode(K key, V value) {
		this.key= key;
		this.value= value;
	}
}