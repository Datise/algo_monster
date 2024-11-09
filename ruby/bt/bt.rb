require_relative '../base/node'

class BTree
  def initialize(nodes)
    self.root = build(nodes)
  end

  def build(nodes, f)
    val = nodes.next rescue nil
    return nil if val.nil? || val == "x"
  
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node.new(f.call(val), left, right)
  end

  def print(root, level=0)
    if level == 0
      puts("\n")
    elsif root != nil:
      print(root.left, level + 1)
      puts(' ' * 4 * level + '->' + node.val)
      print(root.right, level + 1)
    end
  end
end