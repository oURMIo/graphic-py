import vulkan as vk

app_info = vk.VkApplicationInfo(
    pApplicationName="Python Vulkan Example",
    applicationVersion=vk.VK_MAKE_VERSION(1, 0, 0),
    pEngineName="No Engine",
    engineVersion=vk.VK_MAKE_VERSION(1, 0, 0),
    apiVersion=vk.VK_API_VERSION_1_0,
)

create_info = vk.VkInstanceCreateInfo(
    pApplicationInfo=app_info,
    enabledExtensionCount=0,
    ppEnabledExtensionNames=None,
    enabledLayerCount=0,
    ppEnabledLayerNames=None,
)

instance = vk.vkCreateInstance(create_info, None)

physical_devices = vk.vkEnumeratePhysicalDevices(instance)

for device in physical_devices:
    device_properties = vk.vkGetPhysicalDeviceProperties(device)
    print(f"Device Name: {device_properties.deviceName}")
    print(f"API Version: {device_properties.apiVersion}")
    print(f"Driver Version: {device_properties.driverVersion}")
    print(f"Vendor ID: {device_properties.vendorID}")
    print(f"Device ID: {device_properties.deviceID}")
    print(f"Device Type: {device_properties.deviceType}\n")

vk.vkDestroyInstance(instance, None)
