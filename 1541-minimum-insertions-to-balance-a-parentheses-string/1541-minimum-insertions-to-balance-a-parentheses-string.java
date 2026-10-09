class Solution {
    public int minInsertions(String s) {
        int count = 0;
        int res = 0;
        int i = 0;
        int n = s.length();

        while (i < n) {
            if (s.charAt(i) == '(') {
                count++;

            } else {
                if (count > 0) {
                    count--;
                    if (i + 1 < n) {

                        if (s.charAt(i + 1) == ')') {
                            i++;
                        } else {
                            res++;

                        }
                    }else{
                        res++;
                    }
                }else{
                    if (i + 1 < n) {

                        if (s.charAt(i + 1) == ')') {
                            res++;
                            i++;
                        } else {
                            res+=2;

                        }
                    }else{
                        res+=2;
                    }
                }
            }
            i++;
        }
        res += count * 2;

        return res;
    }
}