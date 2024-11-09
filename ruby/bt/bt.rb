require 'pry'
require_relative '../base/node'

class BTree
  attr_accessor :root
  def initialize(nodes)
    self.root = build(nodes.each, :to_i.to_proc)
  end

  def build(nodes, f)
    val = nodes.next rescue nil
    return nil if val.nil? || val == "x"
  
    left = build(nodes, f)
    right = build(nodes, f)
    return Node.new(f.call(val), left, right)
  end

  def print
    def p(node, level)
      if level == 0
        puts("\n")
      elsif node != nil
        p(node.left, level + 1)
        puts(' ' * 4 * level + '->' + node.val)
        p(node.right, level + 1)
      end
    end
    p(self.root, 1)
  end
end

class BTreeLetters < BTree
  attr_accessor :root, :total_nodes
  def initialize(int)
    nodes = ('a'..'z').to_a[0..int -1]
    self.total_nodes = nodes
    self.root = build(self.total_nodes.each)
  end

  def build(nodes)
    val = nodes.next rescue nil
    return "" if val.nil?
    
    children = self.total_nodes.map{|x| val + x}.each { build(nodes) }
    binding.pry
    return NonBNode.new(val, children)
  end

  # def dfs(start_index, path)
  #   if is_leaf(start_index)
  #     report(path)
  #     return

  #   get_edges.each do | edge |
  #     path.add(edge)
  #     dfs(start_index + 1, path)
  #     path.pop()
  #   end
  # end
end 