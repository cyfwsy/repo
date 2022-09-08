class Node(object):
    "構造2,3查找樹節點類"
    def __init__(self,key):
        self.key1 = key #至少一個值，那麽最多是兩個孩子節點
        self.key2 = None #保存兩個值，就有可能使3個孩子節點
        self.left = None
        self.middle = None
        self.right = None
        
    def __repr__(self):
        return '2_3TreeNode({},{})'.format(self.key1,self.key2)
    
    def is_leaf(self):
        #是否為葉子節點
        return self.left is None and self.middle is None and \
            self.right is None
    
    def has_key2(self):
        return self.key2 is not None
    
    def has_key(self,key):
        #2_3 查找樹是否存在該key
        if (self.key1 == key) or (self.key2 is not None and \
            self.key2 == key):
            return True
        else:
            return False
    
    def get_child(self,key):
        #小於key1 查找左邊子樹
        if key < self.key1:
            return self.left
        elif self.key2 is None:
            return self.middle #沒有key2 就把中閒子樹做為右子樹
        elif key < self.key2:
            return self.middle# 有key2 就和key2 比較 比key2 小
        else:
            return self.right # 比key2 d大
        
class TwoThreeTree(object):
    "2_3 查找樹類"
    def __init__(self):
        #初始化，根節點為None
        self.root = None
        
    def is_empty(self):# 是否為空
        return self.root is None
    
    def get(self,key):
        if self.is_empty():
            return None
        else:
            return self._get(self.root,key)
        
    def _get(self,node,key):
        if self.is_empty():
            return None
        elif node is not None and node.has_key(key): #None 在邏輯判斷中相對與False
            return node
        elif node is not None:
            child = node.get_child(key) #沒有找到，繼續尋找孩子節點
            return self._get(child,key)
        else:
            return None
        
    def search(self,key):
        # 查找結點，有則返回True 沒有則返回False
        if self.get(key):
            return True
        else:
            return False
        
        
    def insert(self,key):
        #插入節點
        if self.is_empty():# 如果是空，直接插入
            self.root = Node(key)
        else:
            # 根據情況進行插入 p_key p_ref 為臨時保存
            p_key,p_ref = self._insert(self.root,key)
            if p_key is not None:
                #這裏是最上層，如果還有新插入的元素，則要把中間元素提升為
                #根節點，剩下的兩元素進行拆分，分別放在左子樹(left)和中間
                #子樹(middle)的位置
                new_node = Node(p_key) #這是提升的元素
                new_node.left = self.root
                new_node.middle = p_ref
                self.root = new_node #變成根節點
                
    def _insert(self,node,key):
        if node.has_key(key):# 已經存在節點，無需插入
            return None,None
        elif node.is_leaf():#如果是葉子節點，可以嘗試插入
            return self._add_to_node(node,key,None)
        else: 
            #不是葉子節點，繼續尋找孩子節點
            child = node.get_child(key) #比較插入值大小，判斷在那個子樹
            p_key,p_ref = self._insert(child,key) #遞歸嘗試插入
            if p_key is None:#沒有新插入元素，則無須處理
                return None,None
            else:
                #需要嘗試插入該節點
                return self._add_to_node(node,p_key,p_ref)
            
    def _add_to_node(self,node,key,p_ref):
        if node.has_key2():#如果已經有兩個key，需要插入新元素后拆分剩餘的元素
            return self._split_node(node,key,p_ref)
        else:
            # 只有一個 key 節點
            if key < node.key1: #如果新元素比key1 小，則key 代替key1,key1 變爲key2
                node.key2 = node.key1
                node.key1 = key
                if p_ref is not None:# 如果有新孩子節點
                    node.right = node.middle #原來的中間子樹移到右子樹
                    node.middle = p_ref # 中間子樹指向新孩子節點
            else:
                node.key2 = key #否則新元素為key2
                if p_ref is not None:
                    node.right = p_ref #新孩子節點放在最右邊
            return None,None
        
    def _split_node(self,node,key,p_ref):
        #节点有三个元素时，需要提升中间元素为父节点，拆分剩下的两个元素
        #左边元素用之前的节点，右边元素用新节点
        new_node = Node(None) #新节点给右边元素
        if key < node.key1:#如果新元素比key1小，就提升key1
            p_key = node.key1 #key1为提升元素
            node.key1 = key #新插入元素用key1 节点
            new_node.key1 = node.key2 #key2 是右边新元素
            if p_ref is not None:#如果有新孩子节点
                new_node.left = node.middle #原节点中间节点变为新节点的左节点
                new_node.middle = node.right #原节点的右节点成为新节点的·中间节点
                node.middle = p_ref #中间子树指向新孩子节点
        elif key < node.key2:
            #如果元素大于key1,小于key2,提升新插入的元素
            p_key = key #提升key
            new_node.key1 = node.key2 #key2 是右边新元素
            if p_ref is not None:
                new_node.left = p_ref
                new_node.middle = node.right
        else:
            #如果新插入的元素大于 key2 提升key2
            p_key = node.key2 # key2为提升元素
            new_node.key1 = key #key 是右边新节点
            if p_ref is not None:
                new_node.left = node.right #原节点的右子树成为新节点的左子树
                new_node.middle = p_ref #新孩子节点成为新节点的中间子树
        node.key2 = None #提升后，原节点成为 2 节点
        return p_key,new_node # 返回提升元素和新的孩子节点
    
if __name__ == '__main__':
    t_2_3 = TwoThreeTree()
    for i in [2,7,55,500,21,11,100,99,48,90,430,20,-1000,-3000]:
        t_2_3.insert(i)
    print('---------------------------------')
    print('root node:',t_2_3.root)
    print('root left node:',t_2_3.root.left)
    print('root middle node:',t_2_3.root.middle)
    print('root right node:',t_2_3.root.right)
    t_2_3.insert(66)
    t_2_3.insert(77)
    t_2_3.insert(88)
    print(t_2_3.root)
    print(t_2_3.search(100))
    print(t_2_3.search(0))
    
     
            
                 
            
            
        
                    
            
        
                
        
            
        
        