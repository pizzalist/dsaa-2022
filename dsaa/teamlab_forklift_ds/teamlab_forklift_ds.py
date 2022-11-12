# 모듈 import 파트
from calendar import c
import csv
from datetime import datetime
from http.cookiejar import FileCookieJar
from itertools import count
from operator import indexOf
from os import cpu_count
from platform import node
from time import time
from typing import Any
# Test를 위한 Mock Function 파트


# Class 파트
class ForkliftNode(object):
    def __init__(self, forklift_name : str, location_x : float, location_y : float, iot_datetime : datetime) -> None: #, next : 'Node'
        self._forklift_name = forklift_name
        self._location_x = location_x
        self._location_y = location_y
        self._iot_datetime = iot_datetime
        self._next = None
        # return("Forklift name :", self._forklift_name)
        # return("x coordination :", self._location_x)
        # return("y coordination :", self._location_y)
        # return("Timestamp :", self._iot_datetime)


    def __str__(self):      
        return f'{"Forklift name :"} {self._forklift_name}' +"\n"+ f'{"x coordination :"} {self._location_x}' +"\n"+ f'{"y coordination :"} {self._location_y}' +"\n"+ f'{"Timestamp  :"} {self._iot_datetime}'
                    
        # return str(self._location_x)
        # return str(self._location_y)
        # return str(self._iot_datetime)


    def __repr__(self):     
        return f'{"Forklift name :"} {self._forklift_name}' +"\n"+ f'{"x coordination :"} {self._location_x}' +"\n"+ f'{"y coordination :"} {self._location_y}' +"\n"+ f'{"Timestamp  :"} {self._iot_datetime}'

        # return str(self._location_x)
        # return str(self._location_y)
        # return str(self._iot_datetime)
    

    @property
    def forklift_name(self):
        return self._forklift_name
    @property
    def location_x(self):
        return self._location_x
    @property
    def location_y(self):
        return self._location_y
    @property
    def iot_datetime(self):
        return self._iot_datetime
    @property
    def next(self):
        return self._next

    @forklift_name.setter
    def forklift_name(self, value : str) -> None:
        self._forklift_name = value
    @location_x.setter
    def location_x(self, value : float) -> None:
        self._location_x = value
    @location_y.setter
    def location_y(self, value : float) -> None:
        self._location_y = value
    @iot_datetime.setter
    def iot_datetime(self, value : datetime) -> None:
        self._iot_datetime = value
    @next.setter
    def next(self, value: 'ForkliftNode' ) -> None:
        self._next = value


        

class Node:
    def __init__(self, data: Any = None, next : 'Node' = None) -> None:
        self._data = data
        self._next = None

class LinkedListBag():
    def __init__(self, first_node : 'ForkliftNode' = None) -> None:
        self._head = first_node  
        self._tail = first_node 
        if first_node is not None:
            self._size = 1
        else:
            self._size = 0

    def count(self) -> int:
        counter = 0
        cur_node = self._head
        while cur_node is not None:
            counter += 1
            cur_node = cur_node.next
        return counter

    def append(self, new_node : 'ForkliftNode') -> None:
        if self._size == 0:
            self._head = new_node
            self._tail = new_node 
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1
            

    def insert(self, index_number : int, new_node : 'ForkliftNode') -> bool:
        list_index = 0
        cur_node = self._head
        if index_number == 0:
            self._head = new_node
            new_node.next = cur_node
            self._size += 1
            return True

        while cur_node is not None:
            if list_index == index_number:
                pred_node.next = new_node
                new_node.next = cur_node
                self._size += 1
                return True
            list_index += 1
            pred_node = cur_node 
            cur_node = cur_node.next
        return False

    def remove(self, target_value : datetime) -> bool:
        cur_node = self._head
        pred_node = cur_node 
        
        while cur_node is not None:
            if cur_node.datetime == target_value:
                pred_node.next = cur_node.next
                del(cur_node)
                self._size -= 1
                return True
            pred_node = cur_node 
            cur_node = cur_node.next
        return True        

    def __len__(self):
        return self._size

    def __iter__(self):
        return _BagIterator(self._head)

class _BagIterator():
    def __init__(self, head_node : 'ForkliftNode') -> None:
        self._cur_node = head_node
    
    def __iter__ (self):
        return self
    
    def __next__(self):
        if self._cur_node is None:
            raise StopIteration
        else:
            node = self._cur_node
            self._cur_node = self._cur_node.next
            return node

# 실행 함수 파트
import csv
def load_dataset(filename : str):
    """ 데이터 셋을 입력 받으면 각 지게차 별로 데이터를 이차원 list로 변환하여 반환한다.
    
    Args:
        filename (str) : 지게차의 움직인 데이터를 포함한 파일명

    Returns:
        dataset (dict) : 지게차 이름을 key 값으로, 각 지게차별 정보를 이차원 list로 정리한 값
                         이차원 리스트 값은 아래와 같은 순서로 정돈된다.
                         [emp_x, emp_y, dt_in]
    
    Example:
    >>> import teamlab_forklift_ds as ds
    >>> filename = "forklist_move.csv"
    >>> ds.load_dataset(filename)
        {'TEAM10054239': 
         [['173753.462668852',
           '252318.443103598',
           '2019-06-01 08:30:50.651'],
          ['173725.558119309',
           '252342.150967047',
           '2019-06-01 08:30:50.619'],
          [### 나머지 출력부분은 생략됨]]
        }
    >>> result.keys()
    dict_keys(['TEAM10054239', 'TEAM1007B9625', 'TEAM10083967'])
    >>> len(result.keys())
    3
    """
    command_data = []
    with open (filename, "r") as csvfile:
        datareader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in datareader:
            command_data.append(row)

    data_header = []
    for i in range(len(command_data)):
        if i == 0:
            continue
        if command_data[i][1] not in data_header:
                data_header.append(command_data[i][1])  

    dataset = {}
    for i in range(len(data_header)):
      dataset[data_header[i]] = []

    dataset_list = []
    for i in range(len(data_header)):
        for j in range(len(command_data)):
            if data_header[i] == command_data[j][1]:
                dataset_list.append(command_data[j][3])
                dataset_list.append(command_data[j][4]) 
                dataset_list.append(command_data[j][2])
                dataset[data_header[i]].append(dataset_list)
                dataset_list = []
    
     
    return dataset



def sort_dataset(dataset : dict):
    """생성된 dataset을 넣었을 때 각 지게차별로 시간을 기준으로 sorting하여 값을 반환한다.

    Args:
        dataset (dict) : load_dataset 으로 생성된 dataset dict 파일

    Returns:
        sorted_dataset (dict) : 각 지게차별로 시간 순으로 정렬된 dataset dict 파일
    
    Example:
    >>> import teamlab_forklift_ds as ds
    >>> filename = "forklist_move.csv"
    >>> dataset = ds.load_dataset(filename)
    >>> sorted_result = ds.sort_dataset(dataset)
    >>> print(sorted_result)
        {'TEAM10054239': [['172978.787361283',
                           '252229.400114715',
                           '2019-06-01 08:30:48.797'],
                          ['172997.753770613',
                           '252211.490703829',
                           '2019-06-01 08:30:48.832'],
                          ['173021.175135472',
                           '252193.887723743',
                           '2019-06-01 08:30:48.860'],
                          ['173031.106644024',
                           '252176.916908881',
                           '2019-06-01 08:30:48.896'],
                          [### 나머지 출력부분은 생략됨]]
    """
    # i => index
    sorted_dataset = {}
    for i in dataset.keys():
        # sorted_dataset = dataset #왜 ?? 메모리 사용 공간 더 잡아먹음 : 지우기 
        sorted_dataset[i] = sorted(dataset[i], key=lambda x : x[2])
    
    return sorted_dataset


def build_linkedlistbag(sorted_dataset : dict):
    """이미 sorting된 dataset을 넣었을 때 각 지게차별로 LinkedListBag을 생성하여 반환한다.

    Args:
        dataset (dict) : load_dataset 으로 생성된 dataset dict 파일
                         만일 입력된 데이터셋이 sorting  되지 않았다면, sorting 하여 준다.                       

    Returns:
        linkedlistbag_dict (dict) : 각 지게차별로 생성된 LinkedListBag을 반환한다.
    
    Example:
    >>> sorted_result = ds.sort_dataset(result)
    >>> result = ds.build_linkedlistbag(sorted_result)
    >>> result.keys()
    dict_keys(['TEAM10054239', 'TEAM1007B9625', 'TEAM10083967'])
    >>> for node in result['TEAM10054239']:
            print(node)
        Forklift name : TEAM10054239
        x coordination : 172978.787361283
        y coordination : 252229.400114715
        Timestamp  : 2019-06-01 08:30:48.797000
        Forklift name : TEAM10054239
        x coordination : 172997.753770613
        y coordination : 252211.490703829
        Timestamp  : 2019-06-01 08:30:48.832000
        -------------------------- 생략 --------------
    """
    a = sorted_dataset #모르는 변수 지정 지향
    keys_list = list(sorted_dataset.keys()) # list 제외 가능 ((iterator))
    linkedlist_bag_dict = {}

    
    for i in keys_list: # TEAM..., 
        linkedlist_bag_dict[i] = LinkedListBag()
        for j in a[i] : # ['172978.787361283','252229.400114715','2019-06-01 08:30:48.797'] ['172978.787361283','252229.400114715','2019-06-01 08:30:48.797']
            linkedlist_bag_dict[i].append(ForkliftNode(i, float(j[0]), float(j[1]), datetime.strptime(j[2], "%Y-%m-%d %H:%M:%S.%f")))

  
    return linkedlist_bag_dict


def main():
    DATASET_FILENAME = "forklist_move.csv"
    dataset = load_dataset(DATASET_FILENAME)
    sorted_dataset = sort_dataset(dataset)
    linkedlist_bag_dict = build_linkedlistbag(sorted_dataset)
    
    for node in linkedlist_bag_dict['TEAM10054239']:
            print(node) 
if __name__ == "__main__":
    main()   
