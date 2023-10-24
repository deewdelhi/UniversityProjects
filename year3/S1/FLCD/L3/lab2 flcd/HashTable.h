#pragma once
#include<vector>
#include <iostream>
#include <algorithm>


struct KeyValuePair {
	int key;
	int value;
	KeyValuePair(int key, int value) : key(key), value(value) {};
};
class HashTable
{
private :
	std::vector<std::vector<KeyValuePair>>  *items;
	int size;
public:
	HashTable(int size) {
		this->size = size;
		this->items = new std::vector<std::vector<KeyValuePair>>;
		for (int i = 0; i < size; i++) {
			std::vector<KeyValuePair> v;
			items->push_back(v);
		}
	}
	int getSize() {
		return this->size;
	}

	int hash(int key) {
		return key % size;
	}
	bool contains(int hashValue,int key) {
		auto it = std::find(items[hashValue].begin(), items[hashValue].end(), key);
		return it != items[hashValue].end();
	}

	KeyValuePair add(const KeyValuePair item) {
		int hashValue = hash(item.key);
		if (!contains(hashValue, item.key)) {
			items[hashValue].push_back(item);
		}
	}



};

