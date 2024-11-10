require 'minitest/autorun'
require_relative './btree'
class BTreeTest < Minitest::Test
  def test_bfs
    @tree = BTree.new(["3","4","5","x","x","7","x"])
    result = @tree.levels
    assert_equal([[3], [4], [7, 5]], result)
  end

  def test_zig_zag
    @tree = BTree.new(["1", "2", "4", "x", "x", "5", "x", "x", "3", "6", "x", "x", "7", "x", "x"])    
    @tree.print
    result = @tree.zig_zag
    assert_equal([[1], [3, 2], [4, 5, 6, 7]], result)
  end

  def test_min_depth
    @tree = BTree.new(["1", "2", "4", "x", "x", "5", "x", "x", "3", "6", "x", "x", "7", "x", "x"])    
    result = @tree.min_depth
    assert_equal(2, result)
  end
end