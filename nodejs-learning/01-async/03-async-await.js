// async/await - 最简洁的写法
function fetchUser(id) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (id > 0) {
        resolve({ id, name: `User ${id}` })
      } else {
        reject(new Error('Invalid ID'))
      }
    }, 1000)
  })
}

// 使用 async/await
async function main() {
  console.log('开始...')
  
  try {
    const user1 = await fetchUser(1)
    console.log('获取到用户:', user1)
    
    const user2 = await fetchUser(2)
    console.log('获取到第二个用户:', user2)
    
    // 并行请求
    const [user3, user4] = await Promise.all([
      fetchUser(3),
      fetchUser(4)
    ])
    console.log('并行获取:', user3, user4)
    
  } catch (err) {
    console.error('错误:', err.message)
  }
}

main()
