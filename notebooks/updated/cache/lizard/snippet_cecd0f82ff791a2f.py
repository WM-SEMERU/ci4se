def __roll(self, unrolled):
    rolled = []
    index = 0
    for count in range(len(self.__sizes) - 1):
        in_size = self.__sizes[count]
        out_size = self.__sizes[count + 1]
        theta_unrolled = np.matrix(unrolled[index:index + (in_size + 1) *
            out_size])
        theta_rolled = theta_unrolled.reshape((out_size, in_size + 1))
        rolled.append(theta_rolled)
        index += (in_size + 1) * out_size
    return rolled