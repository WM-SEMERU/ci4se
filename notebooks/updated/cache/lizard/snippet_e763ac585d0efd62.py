def balanced_accuracy(y_true, y_pred):
    all_classes = list(set(np.append(y_true, y_pred)))
    all_class_accuracies = []
    for this_class in all_classes:
        this_class_sensitivity = 0.0
        this_class_specificity = 0.0
        if sum(y_true == this_class) != 0:
            this_class_sensitivity = float(sum((y_pred == this_class) & (
                y_true == this_class))) / float(sum(y_true == this_class))
            this_class_specificity = float(sum((y_pred != this_class) & (
                y_true != this_class))) / float(sum(y_true != this_class))
        this_class_accuracy = (this_class_sensitivity + this_class_specificity
            ) / 2.0
        all_class_accuracies.append(this_class_accuracy)
    return np.mean(all_class_accuracies)