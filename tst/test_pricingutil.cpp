#include <gtest/gtest.h>
#include <pricingutil.h>

TEST(Tests, accuracyTest) {
    PricingUtil pricingUtil;
    float res = pricingUtil.calcVal(2.0, 0.2, 2.0);
    EXPECT_EQ(pricingUtil.getVal(), res);
}

TEST(Tests, valueTest) {
    PricingUtil pricingUtil;
    float res = pricingUtil.calcVal(2.0, 0.2, 2.0);
    EXPECT_NEAR(pricingUtil.getVal(), 4.4, 1e-4);
}

TEST(Tests, zeroInterest) {
    PricingUtil pricingUtil;
    float res = pricingUtil.calcVal(2.0, 0.0, 2.0);
    EXPECT_NEAR(pricingUtil.getVal(), 3.6, 1e-4);
}

TEST(Tests, negativeInterest) {
    PricingUtil pricingUtil;
    float res = pricingUtil.calcVal(2.0, -0.2, 2.0);
    EXPECT_NEAR(pricingUtil.getVal(), 2.8, 1e-4);
}

TEST(calcValTest, zeroOleo) {
    PricingUtil pricingUtil;
    float res = pricingUtil.calcVal(2.0, 0.2, 0.0);
    EXPECT_NEAR(pricingUtil.getVal(), 0.0, 1e-4);
}

TEST(calcValTest, negativeOleo) {
    PricingUtil pricingUtil;
    float res = pricingUtil.calcVal(2.0, 0.2, -2.0);
    EXPECT_NEAR(pricingUtil.getVal(), -4.4, 1e-4);
}

TEST(calcValTest, zeroPrev) {
    PricingUtil pricingUtil;
    float res = pricingUtil.calcVal(0.0, 0.2, 2.0);
    EXPECT_NEAR(pricingUtil.getVal(), 0.0, 1e-4);
}

TEST(calcValTest, negativePrev) {
    PricingUtil pricingUtil;
    float res = pricingUtil.calcVal(-2.0, 0.2, 2.0);
    EXPECT_NEAR(pricingUtil.getVal(), -4.4, 1e-4);
}

