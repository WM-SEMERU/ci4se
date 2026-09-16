def print_progress(self, i, current_params):
    for split in range(1, 11):
        if i == round(self.iterations / 10 * split) - 1:
            post = -self.full_neg_posterior(current_params)
            approx = self.create_normal_logq(current_params)
            diff = post - approx
            if not self.quiet_progress:
                print(str(split) + '0% done : ELBO is ' + str(diff) +
                    ', p(y,z) is ' + str(post) + ', q(z) is ' + str(approx))