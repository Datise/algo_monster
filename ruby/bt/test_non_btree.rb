require 'minitest/autorun'
require_relative './non_btree'
class TernaryTreeTest < Minitest::Test
  def test_ternary_paths
    @tree = NonBTree.new(["1", "3", "2", "0", "3", "0", "4", "3", "5", "0", "6", "0", "7", "0"])
    res = @tree.ternary_tree_paths
    assert_equal ['1->2', '1->3', '1->4->5', '1->4->6', '1->4->7'], res
  end
end

class NonBTreeLettersTest < Minitest::Test
  def test_letter_combo_simple
    @combos = letter_combination_simple(2)
    assert_equal ['aa','ab', 'ba', 'bb'], @combos
  end

  def test_letter_compbo_long
    @combos = letter_combination_simple(4)
    assert_equal ["aaaa", "aaab", "aaba", "aabb", "abaa", "abab", "abba", "abbb", "baaa", "baab", "baba", "babb", "bbaa", "bbab", "bbba", "bbbb"], @combos
  end

  def test_letter_combination_phone
    @combos = letter_combination_phone("56")
    assert_equal ["jm","jn","jo","km","kn","ko","lm","ln","lo"], @combos
  end

  def test_palindromes
    @combos = palindromes("aab")
    assert_equal [["aa","b"],["a","a","b"]], @combos
  end
end