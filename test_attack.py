import torchattacks

attacker = torchattacks.PGD()

# random labels as target labels. 使用随机标签作为目标标签。即每个样本的目标标签随机生成，与原始标签无关。
attacker.set_mode_targeted_random()

# labels with the k-th smallest probability as target labels. 使用模型对当前样本预测概率第 k 小的类别作为目标标签。换句话说，模型认为最不可能是该类别的标签被选为攻击目标。
attacker.set_mode_targeted_least_likely(kth_min=2)

# labels obtained by mapping function as target labels.
# shift all class loops one to the right, 1=>2, 2=>3, .., 9=>0  使用自定义的映射函数来生成目标标签。在这个例子中，映射函数将原始标签加 1，然后对 10 取模 (% 10) 来生成新的目标标签。这意味着标签 0 会被映射为 1，标签 9 会被映射为 0，形成一个循环。
attacker.set_mode_targeted_by_function(target_map_function=lambda images, labels:(labels+1)%10)

attacker.set_mode_targeted_by_label(quiet=True)
  # shift all class loops one to the right, 1=>2, 2=>3, .., 9=>0  这个方法允许你直接指定目标标签，而不是通过某种规则或函数生成。在这个例子中，target_labels 是直接计算的 (labels + 1) % 10，然后将其作为攻击的目标标签。
target_labels = (labels + 1) % 10
adv_images = attacker(images, target_labels)