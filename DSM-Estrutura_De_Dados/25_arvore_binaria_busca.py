from lib.binary_search_tree import BinarySearchTree

arvore = BinarySearchTree()

arvore.insert(23)
arvore.insert(39)
arvore.insert(11)
arvore.insert(31)
arvore.insert(17)
arvore.insert(0)
arvore.insert(43)
arvore.insert(7)
arvore.insert(29)
arvore.insert(13)
arvore.insert(53)
arvore.insert(19)
arvore.insert(47)
arvore.insert(5)
arvore.insert(59)

print("PERCURSO EM-ORDEM:")
arvore.in_order_traversal(print)

print("*" * 50)

print("PERCURSO PRÉ-ORDEM:")
arvore.pre_order_traversal(print)

print("*" * 50)

print("PERCURSO PÓS-ORDEM:")
arvore.post_order_traversal(print)

print("*" * 50)

# Exclusão de um nodo de grau 0
arvore.remove(29)

print("PERCURSO EM-ORDEM APÓS EXCLUSÃO DO 29 (GRAU 0):")
arvore.in_order_traversal(print)

print("*" * 50)

# Exclusão de um nodo grau 1 com lado esquerdo
arvore.remove(7)

print("PERCURSO EM-ORDEM APÓS EXCLUSÃO DO 7 (GRAU 1 COM LADO ESQ.):")
arvore.in_order_traversal(print)

print("*" * 50)

# Exclusão de um nodo grau 1 com lado direito
arvore.remove(43)

print("PERCURSO EM-ORDEM APÓS EXCLUSÃO DO 43 (GRAU 1 COM LADO DIR.):")
arvore.in_order_traversal(print)

print("*" * 50)

# Exclusão de um nodo grau 2
arvore.remove(23)

print("PERCURSO EM-ORDEM APÓS EXCLUSÃO DO 23 (GRAU 2):")
arvore.in_order_traversal(print)