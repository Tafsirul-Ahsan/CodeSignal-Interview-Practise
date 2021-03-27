// Singly-linked lists are already defined with this interface:
// class ListNode<T> {
//   ListNode(T x) {
//     value = x;
//   }
//   T value;
//   ListNode<T> next;
// }
//

ListNode < Integer > addTwoHugeNumbers(ListNode < Integer > a, ListNode < Integer > b) {
  int i = 0;
  BigInteger total = null;
  String firstNumber = "",
  secondNumber = "";
  while (a != null) {
    if (i == 0) {
      firstNumber = "" + a.value;
    } else {
      firstNumber = firstNumber + "" + String.format("%04d", a.value);
    }
    a = a.next;
    i++;
  }
  i = 0;
  while (b != null) {
    if (i == 0) {
      secondNumber = "" + b.value;
    } else {
      secondNumber = secondNumber + "" + String.format("%04d", b.value);
    }
    b = b.next;
    i++;
  }
  i = 0;
  total = new BigInteger("" + firstNumber).add(new BigInteger("" + secondNumber));
  ListNode < Integer > listNode = new ListNode(0);
  ListNode temp = null;
  while (total.signum() > 0) {
    System.out.println(total.remainder(new BigInteger("" + 10000)));
    int remaindervalue = total.remainder(new BigInteger("" + 10000)).intValue();
    if (i == 0) {
      listNode = new ListNode(remaindervalue);
      temp = listNode;
    } else {
      temp.next = new ListNode(remaindervalue);
      temp = temp.next;
    }
    total = total.divide(new BigInteger("" + 10000));
    i++;
  }
  ListNode < Integer > prev = null,
  current = listNode,
  next;
  while (current != null) {
    next = current.next;
    current.next = prev;
    prev = current;
    current = next;
  }
  listNode = prev;
  return listNode;
}

