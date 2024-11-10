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

  def levels
    res = []
    queue = [self.root]
    while queue.length > 0
      new_level = []
      queue.length.times do
        node = queue.pop 
        new_level.append(node.val)
        node.children.each do |child|
          next if child.nil?
          queue.append(child)
        end
      end
      res.append(new_level)
    end
    return res
  end

  def zig_zag
    res = []
    queue = [self.root]
    left_to_right = false
    while queue.length > 0
      prev_level = []
      queue.length.times do |index|
        node = queue.shift
        if left_to_right
          prev_level.unshift(node.val)
        else
          prev_level.append(node.val)
        end
        node.children.each do |child|
          next if child.nil?
          queue.append(child)
        end
      end
      left_to_right = !left_to_right
      res.append(prev_level)
    end
    return res
  end

  def min_depth
    res = []
    queue = [self.root]
    while queue.length
      prev_level = []
      queue.length.times do 
        node = queue.shift 
        return res.length if node.nil?
        prev_level.append(node)
        node.children.each do |child|
          return res.length if child.nil?
          queue.append(child)
        end
      end
      res.append(prev_level)
    end
    return res.length
  end

  def print
    def p(node, level)
      if level == 0
        puts("\n")
      elsif node != nil
        p(node.left, level + 1)
        puts(' ' * 4 * level + '->' + node.val.to_s)
        p(node.right, level + 1)
      end
    end
    p(self.root, 1)
  end
end
