"""
Display scatter plots to see the exam results based on hours studied and breaks taken
Make it as much readable as possible
"""
import matplotlib.pyplot as plt

hours_studied = [1, 1.5, 2, 2.5, 3, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5]
breaks_taken = [0, 2, 1, 3, 0, 1, 2, 0, 3, 0, 2, 1, 3, 0, 2] 
exam_scores = [52, 54, 57, 59, 63, 67, 72, 76, 78, 82, 85, 88, 90, 93, 95]

plt.scatter(hours_studied, exam_scores, color="b", alpha=0.3, label="Hours studied" )
plt.scatter(breaks_taken, exam_scores, color="g", alpha=0.3, label="Breaks taken in hours")
plt.xlabel("Hours")
plt.ylabel("Scores in %")
plt.grid(True)
plt.legend()


plt.show()




"""

plt.scatter(hours_studied, exam_scores, color="g", label="First set")
plt.scatter(exam_scores, breaks_taken, color="r", label="Second set")
    
plt.title("See")
plt.xlabel("Hours studies")
plt.ylabel("Breaks taken")
plt.grid(True)
plt.legend()

plt.show()
"""