require 'minitest/autorun'
require_relative './non_b_tree'
class TernaryTreeTest < Minitest::Test
  def test_ternary_paths
    @tree = NonBTree.new(["1", "3", "2", "0", "3", "0", "4", "3", "5", "0", "6", "0", "7", "0"])
    res = @tree.ternary_tree_paths
    assert_equal ['1->2', '1->3', '1->4->5', '1->4->6', '1->4->7'], res
  end
end