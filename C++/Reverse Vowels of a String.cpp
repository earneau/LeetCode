// Link to the exercise : https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75

// INSTRUCTIONS //

// Given a string s, reverse only all the vowels in the string and return it.
// The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

// EXERCISE //

class Solution {
public:
    string reverseVowels(string s) {
        string vowels = "aeiouAEIOU";  // Include lowercase and uppercase vowels
        string extractedVowels = "";
        string result = s;

        // first pass: extract vowels from the string
        for (char ch : s) {
            if (vowels.find(ch) != string::npos) {
                extractedVowels.push_back(ch);
            }
        }

        // Second pass: replace vowels in the reverse order
        int cpt = extractedVowels.size() - 1;
        for (int i = 0; i < s.length(); i++) {
            if (vowels.find(s[i]) != string::npos) {
                result[i] = extractedVowels[cpt--]; // Place vowels in reverse order
            }
        }

        return result;
    }
};
