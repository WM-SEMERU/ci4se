def getVulkanDeviceExtensionsRequired(self, pchValue, unBufferSize):
    fn = self.function_table.getVulkanDeviceExtensionsRequired
    pPhysicalDevice = VkPhysicalDevice_T()
    result = fn(byref(pPhysicalDevice), pchValue, unBufferSize)
    return result, pPhysicalDevice